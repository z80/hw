var SCthegnome = null;
var SCthechat = null;
var SCchatxpos;
var SCchatypos;
var SCchattop;
var SCgnomexpos;
var SCgnomeypos;
var SCoriginalgnomeypos;
var SCgnometop;
var SCopacity;
var SCgnomeopacity;
var SCstepforward;
var SCinterval;
var SCinterval2;
var SCid;
var SCwidth;
var SCheight;
var SCadditionalheight;
var SCinvitationPhrase;
var SCongoingPhrase;
var SCrequestColor;
var SCchatColor;
function SCyeswecan ()
{
	SCthechat.innerHTML = "<p align=\"center\">Great!</p>";
	SCstepforward = 0;
	SCinterval2 = setInterval (SCenlarge, 100);
}
function SCenlarge ()
{
	SCstepforward += 40;
	SCchatypos -= 40;
	SCgnomeypos -= 40;
	SCthechat.style.height = (SCstepforward+SCheight) + "px";
	SCthegnome.style.top = SCgnomeypos + "px";
	if ( SCstepforward >= SCadditionalheight ) {
		clearInterval (SCinterval2);
		SCthechat.innerHTML = "<span style=\"float:left;padding-bottom:5px;\">"+SCongoingPhrase+"</span><span style=\"float:right;padding-bottom:5px;\"><a href=\"javascript:SCnowecant()\">[close]</a></span><iframe width=\"100%\" height=\"90%\" src=\"https://services.sitecharm.com/realtime/chat.php?id="+SCid+"&speaker=1\" style=\"clear:both;background:"+SCchatColor+";\" scrolling=\"auto\"/>";
	}
	window.onscroll();
}
function SCnowecant ()
{
	document.body.removeChild (SCthechat);
	document.body.removeChild (SCthegnome);
	SCthechat = null;
	SCthegnome = null;
}
function SCscrolling () {
	if ( SCthechat ) {
		var SCnewxscroll = document.documentElement.scrollLeft || document.body.scrollLeft;
		var SCnewyscroll = document.documentElement.scrollTop || document.body.scrollTop;
		delete SCthechat.style.bottom;
		delete SCthechat.style.right;
		SCchattop = SCchatypos + SCnewyscroll;
		SCthechat.style.top = SCchattop + "px";
		SCthechat.style.left = (SCchatxpos + SCnewxscroll) + "px";
	}
	if ( SCthegnome ) {
		var SCnewxscroll = document.documentElement.scrollLeft || document.body.scrollLeft;
		var SCnewyscroll = document.documentElement.scrollTop || document.body.scrollTop;
		delete SCthegnome.style.bottom;
		delete SCthegnome.style.right;
		SCgnometop = SCgnomeypos + SCnewyscroll;
		SCthegnome.style.top = SCgnometop + "px";
		SCthegnome.style.left = (SCgnomexpos + SCnewxscroll) + "px";
	}
}
function SChovergnome ()
{
	SCgnomeypos -= 10;
	SCgnomeopacity += .05;
	if ( SCgnomeopacity > .8 )
		SCgnomeopacity = .8;
	SCthegnome.style.top = SCgnomeypos + "px";
	SCthegnome.style.opacity = SCgnomeopacity;
	if ( SCgnomeypos <= SCoriginalgnomeypos - SCheight ) {
		clearInterval (SCinterval);
		SCmakeChat2();
	}
	window.onscroll();
}
function SCmakeChat (id, ltc)
{
	SCsetLtField (ltc);
	SCid = id;
	if ( !SCwidth )
		SCwidth = 300;
	if ( !SCheight )
		SCheight = 80;
	if ( !SCadditionalheight )
		SCadditionalheight = 300;
	if ( !SCinvitationPhrase )
		SCinvitationPhrase = "Can we chat?";
	if ( !SCongoingPhrase )
		SCongoingPhrase = "Chatting...";
	if ( !SCrequestColor )
		SCrequestColor = "#a0a0a0";
	if ( !SCchatColor )
		SCchatColor = "#fff";
	SCthegnome = new Image();
	SCthegnome.src = "http://sitecharm.com/images/gnome.gif";
	setTimeout (SCmakeChat_continue, 4000);
}
function SCmakeChat_continue ()
{
	SCthegnome.style.position = "absolute";
	SCthegnome.style.right = "0px";
	SCthegnome.style.bottom = "0px";
	SCgnomeopacity = 0.0;
	SCthegnome.style.opacity = SCgnomeopacity;
	document.body.appendChild (SCthegnome);
	SCgnomexpos = SCthegnome.offsetLeft;
	SCgnomeypos = SCthegnome.offsetTop;
	SCoriginalgnomeypos = SCthegnome.offsetTop;
	window.onscroll = SCscrolling;
	window.onscroll();
	SCgnomeypos += 223;
	SCthegnome.style.top = SCgnomeypos + "px";
	SCinterval = setInterval (SChovergnome, 100);
}
function SCmakeChat2 ()
{
	SCthechat = document.createElement("div");
	SCthechat.style.position = "absolute";
	SCthechat.style.height = SCheight + "px";
	SCthechat.style.bottom = "0px";
	SCthechat.style.width = SCwidth + "px";
	SCthechat.style.right = "0px";
	SCthechat.style.background = SCrequestColor;
	SCthechat.style.borderRadius = "5px";
	SCthechat.innerHTML = "<p align=\"center\">" + SCinvitationPhrase
	  + "<br/><button onclick=\"SCyeswecan()\">Yes</button>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<button onclick=\"SCnowecant()\">No</button></p>";
	SCopacity = 0;
	SCthechat.style.opacity = SCopacity * 0.1;
	document.body.appendChild (SCthechat);
	SCchatxpos = SCthechat.offsetLeft;
	SCchatypos = SCthechat.offsetTop;
	window.onscroll();
	SCinterval = setInterval (
		function(){
			SCthechat.style.opacity = (++SCopacity)*.1;
			if ( SCopacity >= 10 )
				clearInterval(SCinterval);
		},
		100);
}

function SCsetLtField (ltc)
{
	var SCdiv = document.getElementById("longTermField");
	if ( SCdiv )
		SCdiv.value = ltc;
}

var SCimg = document.createElement("img");
var SCbody = document.getElementsByTagName("body")[0];
SCimg.src = "http://advanced.sitecharm.com:8080/?387&"+escape(document.referrer);
SCimg.style.display = "none";
SCbody.appendChild(SCimg);

var sitecharm = {
	event: function (name) {
		var img = document.createElement("img");
		var body = document.getElementsByTagName("body")[0];
		img.src = "http://advanced.sitecharm.com:8080/e?387&"+escape(name);
		img.style.display = "none";
		body.appendChild(img);
	}
};
