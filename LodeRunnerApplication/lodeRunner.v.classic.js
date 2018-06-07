var classicData = [];

$.get("http://localhost:8498/api/Maps/Level", function (data) {
    classicData[0] = data;
});