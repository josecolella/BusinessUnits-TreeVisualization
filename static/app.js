$("#save").click(function() {
    console.log("Hello@!!!");
    //Add CSS to the SVG
    var css = d3.select("style").node();

    var svg = d3.select("svg");
    svgNode = svg.node();
    svgNode.insertBefore(css, svgNode.firstChild);

    var html = d3.select("svg")
        .attr("title", "test2")
        .attr("version", 1.1)
        .attr("xmlns", "http://www.w3.org/2000/svg")
        .node().outerHTML;


    var blob = new Blob([html], {type: "image/svg+xml"});
    saveAs(blob, "myProfile.svg");
});