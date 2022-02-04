var classicData = [];
classicData[0] = "                  S         " +
    "                  S         " +
    "#######H#######   S         " +
    "       H----------S    $    " +
    "       H    ##H   #######H##" +
    "       H    ##H          H  " +
    "     0 H    ##H        0 H  " +
    "##H#####    ########H#######" +
    "  H      --         H       " +
    "  H                 H       " +
    "#########H######X###H       " +
    "         H          H       " +
    "         H----------H   $   " +
    "    H######         #######H" +
    "    H         &  $ $$      H" +
    "######################@#####";

$.get("http://localhost:8498/api/Maps/Level", function (data) {
   classicData[1] = data;
});