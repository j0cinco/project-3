


// This function is used in optionChanged which feeds it the metadata.
// The existing unordered list is cleared and a new one takes the place.
function Meta(data) {
    var div = d3.select("#sample-metadata");
    div.html("")
    var list = div.append("ul");
    Object.entries(data).forEach(([key, value]) => {
        list.append("li").text(key + ": " + value);
     });
}



