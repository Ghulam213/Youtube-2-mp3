const convertBtn = $("#conBtn");
const cssNew = {
	"border-radius": "50%",
	"height": "40px",
	"width": "40px",
	"font-size": "25px",
	"padding": "0px 0px 4px 0px",
	// "background-color" : "#28a745",
	// "border-color" : "#28a745"
};
convertBtn.click(function(){
	console.log("activated")
	$(this).animate(cssNew, 500)
	$(this).html("<strong>&#10003</strong>")
	$(this).removeClass("btn btn-outline-primary my-2 my-sm-0").addClass("btn btn-success");
})