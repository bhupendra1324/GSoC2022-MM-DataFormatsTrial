var viewer = new Cesium.Viewer("cesiumContainer");
var tileset = viewer.scene.primitives.add(
  new Cesium.Cesium3DTileset({
    url: "./3dtile_nyc/tileset.json",
  })
);
Cesium.when(tileset.readyPromise).then(function (tileset) {
  viewer.flyTo(tileset);
});
