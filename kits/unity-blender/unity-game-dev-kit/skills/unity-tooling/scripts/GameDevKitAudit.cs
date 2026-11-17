using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;

namespace GameDevKit
{
    public static class Audit
    {
        [Serializable] public class ModelInfo
        {
            public string path;
            public float importScale;
            public long triangles;
        }
        [Serializable] public class Report
        {
            public string unityVersion;
            public string scope = "Asset inventory; no scene mutation or artistic approval";
            public string[] enabledScenes;
            public ModelInfo[] models;
            public int materialCount;
            public string[] warnings;
        }

        public static long CountTriangles(Mesh mesh)
        {
            long count = 0;
            for (int i = 0; i < mesh.subMeshCount; i++)
                if (mesh.GetTopology(i) == MeshTopology.Triangles)
                    count += (long)mesh.GetIndexCount(i) / 3;
            return count;
        }

        [MenuItem("Tools/Game Dev Kit/Audit assets")]
        public static void Run()
        {
            var warnings = new List<string>();
            var scenes = EditorBuildSettings.scenes.Where(s => s.enabled).Select(s => s.path).ToArray();
            if (scenes.Length == 0) warnings.Add("No enabled build scenes; check the intended Build Profile.");
            foreach (var scene in scenes)
                if (AssetDatabase.LoadAssetAtPath<SceneAsset>(scene) == null)
                    warnings.Add("Missing enabled scene: " + scene);
            var models = new List<ModelInfo>();
            foreach (var guid in AssetDatabase.FindAssets("t:Model", new[] { "Assets" }))
            {
                string path = AssetDatabase.GUIDToAssetPath(guid);
                var importer = AssetImporter.GetAtPath(path) as ModelImporter;
                if (importer == null) continue;
                var meshes = AssetDatabase.LoadAllAssetsAtPath(path).OfType<Mesh>();
                models.Add(new ModelInfo { path = path, importScale = importer.globalScale,
                    triangles = meshes.Sum(m => CountTriangles(m)) });
            }
            var materials = AssetDatabase.FindAssets("t:Material", new[] { "Assets" });
            foreach (string guid in materials)
            {
                string path = AssetDatabase.GUIDToAssetPath(guid);
                var material = AssetDatabase.LoadAssetAtPath<Material>(path);
                if (material != null && (material.shader == null || material.shader.name == "Hidden/InternalErrorShader"))
                    warnings.Add("Missing/error shader: " + path);
            }
            var report = new Report { unityVersion = Application.unityVersion, enabledScenes = scenes,
                models = models.OrderBy(m => m.path).ToArray(), materialCount = materials.Length,
                warnings = warnings.ToArray() };
            Directory.CreateDirectory("Library/GameDevKit");
            File.WriteAllText("Library/GameDevKit/audit.json", JsonUtility.ToJson(report, true));
            Debug.Log("GAME_DEV_KIT_AUDIT_OK models=" + models.Count + " warnings=" + warnings.Count);
        }

        public static void RunSelfTest()
        {
            var mesh = new Mesh();
            try
            {
                mesh.vertices = new[] { Vector3.zero, Vector3.right, Vector3.up, Vector3.one };
                mesh.subMeshCount = 2;
                mesh.SetTriangles(new[] { 0, 1, 2 }, 0);
                mesh.SetIndices(new[] { 2, 3 }, MeshTopology.Lines, 1);
                if (CountTriangles(mesh) != 1) throw new Exception("Triangle topology regression");
            }
            finally { UnityEngine.Object.DestroyImmediate(mesh); }
            Run();
            Debug.Log("GAME_DEV_KIT_SELFTEST_PASS");
        }
    }
}
