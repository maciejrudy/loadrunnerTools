import fafaafdsa.h;
import fafaafdsa.h;
import fafaafdsa.h;


import fafaafdsa.h;

fas saflfls jdl

fsdalfjals 
fasdfasf
fasfas


fasfsfkjh fsd fksd
ffas


fdafasfasfas


fasfafa


//////BODY PARAMS
web_custom_request1(
"aaa=bbb"
"cccccccccc"
"some parameters"
"Body=a111="
"1&a2=2&a3=333"
"3333333"
"3&a4=4",LAST);

web_custom_request2(
"aaa=bbb"
"cccccccccc"
"some parameters"
"Body=a222"
"&a2=2&a3=333"
"33"
"33333&a"
"4",
LAST);

fadfa fasf saf afa
fasdafafa

web_custom_request3(
	"aaa=bbb"
	"cccccccccc"
	"some parameters"
	"Body=a333"
	"&a2=2&a3=333"
	"3333333&"
	"a4=4&"
	,LAST);

web_custom_request3.1(
	"aaa=bbb"
	"cccccccccc"
	"some parameters"
	"Body=a333"
	"&a2=2&a3=333"
	"3333333&"
	"a4&",
	LAST);


///////JSON
web_custom_request4json(
"some parameters"
"Body={\"aaa\": \"va\"}",LAST);

web_custom_request5json(
"some parameters"
"Body={\"ccc\": \"vc\", \"bbb\":\"vb\"}",
LAST);

web_custom_request6json(
"some parameters"
"Body={\"ddd\":"
"\"vd\", \"bbb\""
":\"vb\"}",
LAST);

web_custom_request7json(
	"some parameters"
"Body=[{\"eee\": \"ve\"},{\"bbb\": \"vb\"}]",LAST);

web_custom_request8json(
	"some parameters"
	"Body=[{\"fff\": \"vf\"},{\"bbb\": \"vb\"}]",
	LAST);

web_custom_request8.1json(
	"some parameters"
	"Body=["
	"{\"fff\": \"vf\"},  \\n   {\"bbb\": \"vb\",\"ddd\": \\n\"vd\", \"parent\":"
	"{\"parA\":\"valA\",\"parB\":222}},{\"namenull\":null}]",
	LAST);

web_custom_request8.2json(
	"some parameters",
	"Body={\"jsonData\":"
	"\"  {\\\"nestedKey\\\": \\\"nestedValue\\\"}   \""
	"}",
	LAST);

web_custom_request8.3json(
	"some parameters"
	"Body={\"ggg"
	"\":\"vg\", \""
	"gg"
	"ggg"
	"\""
	":"
	"\""
	"vggggg"
	"\""
	}",
	LAST);


web_custom_request8.4json(
	"some parameters84.1",
	"some parameters84.2",
"Body={\"opsname\":null,\"vars\":{},\"query\":\"{\\n bakerA: bakeriInfo(id: \\\"aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee\\\") {\\n baker {\\n id\\n name {\\n es\\n }\\n }\\n address {\\n company\\n city\\n postalCode\\n }\\n bakerRolls (cookLengua: \\\"es\\\") {\\n results {\\n rollShape\\n cookLengua\\n documentType\\n content\\n }\\n }\\n provisioningOptions "
"{\\n  results {\\n id\\n rollName\\n rollDescription\\n provisioningDuration {\\n minDiameter\\n maxDiameter\\n weight\\n }\\n }\\n }\\n }\\n bakerB: bakerInfo (id: \\\"baaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee\\\") {\\n baker {\\n id\\n name {\\n es\\n }\\n }\\n address {\\n company\\n city\\n postalCode\\n }\\n bakerRolls (cookLengua: \\\"es\\\") {\\n results "
"{\\n rollShape\\n cookLengua\\n documentType \\n content\\n }\\n }\\n provisioningOptions {\\n results {\\n id\\n rollName\\n rollDescription\\n provisioningDuration {\\n minDiameter\\n maxDiameter\\n weight\\n }\\n }\\n }\\n }\\n bakerC: bakerinfo(id: \\\"caaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee\\\") {\\n baker {\\n id\\n name {\\n es\\n }\\n }\\n "
"address {\\n company\\n city\\n postalCode\\n }\\n bakerRolls (cookLengua: \\\"es\\\") {\\n results {\\n rollShape\\n cookLengua\\n documentType\\n content\\n }\\n }\\n provisioningoOptions {\\n results {\\n id\\n rollName\\n rollDescription\\n provisioningDuration {\\n minDiameter\\n maxDiameter\\n weight\\n }\\n }\\n }\\n }\\n bakerD: bakerinfo"
"(id: \\\"daaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee\\\") {\\n baker {\\n id\\n name {\\n es\\n }\\n }\\n address {\\n company \\n city\\n postalCode\\n }\\n bakerRolls (cookLengua: \\\"es\\\") {\\n results {\\n rollShape\\n cookLengua\\n documentType\\n content\\n }\\n }\\n provisioningOptions {\\n results {\\n id\\n rollName\\n rollDescription\\n"
"provisioningDuration {\\n minDiameter\\n maxDiameter\\n weight\\n }\\n }\\n }\\n }\\n}\\n\"}",
LAST);



/////////////////XML

web_custom_requestA.1xml(
	"some parameters"
	"Body=<a><b>c</b></a>",
	LAST);

web_custom_requestA.2xml(
	"some parameters"
	"Body=<a>"
	"<b>"
	"c"
	"</b>"
	"</a>",LAST);

web_custom_requestA.3xml(
	"some parameters"
	"Body=<"
	"a"
	">"
	"<"
	"b"
	">"
	"c"
	"<"
	"/"
	"b"
	"></a"
	">", LAST);

web_custom_requestA.4xml(
	"some parameters"
	"Body=<?xml version=\"1.0\" ?><a x=\"x\" y=\"y\"><b z=\"zzzz\">c</b></a>",
	LAST);



fadfa fasf saf afa
fasdafafa


web_custom_requestBmultipart(
	"some parameters"
"Body=--boundary42"
"Content-Type: text/plain; charset=us-ascii "
""
"//based on RFC1341...plain text version of message goes here.... "
""
"--boundary42"
"Content-Type: text/richtext"
""
".... richtext version of same message goes here ..."
"--boundary42"
"Content-Type: text/x-whatever "
""
".... fanciest formatted version of same  message  goes  here"
"--boundary42--"
,LAST);



fadfa fasf saf afa
fasdafafa
fadfa fasf saf afa
fasdafafa
