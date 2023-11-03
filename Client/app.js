

function getfloors(){
    var uifloor = document.getElementsByName("uifloor");
    for(var i in uifloor){
        if(uifloor[i].checked){
            return parseInt(i)+1;
        }
    }
    return -1;
}

function getview(){
    var uiview = document.getElementsByName("uiview");
    for(var i in uiview){
        if(uiview[i].checked){
            return parseInt(i);
        }
    }
    return -1;
}

function getcondition(){
var uicondition = document.getElementsByName("uicondition");
    for(var i in uicondition){
        if(uicondition[i].checked){
            return parseInt(i)+1;
        }
    }
    return -1;
}


function onClickedEstimatePrices(){
    console.log("Estimate price button clicked");
    var living_area = document.getElementById("uisqft");
    var bedroom = document.getElementById("uibedroom");
    var bathroom= document.getElementById("uibathroom");
    var lot_area = document.getElementById("uiltarea");
    var floors = getfloors();
    var view = getview();
    var condition = getcondition();
    var basement_area = document.getElementById("uibasement");
    var city = document.getElementById("uicity");
    var est_price = document.getElementById("uiestimatedprice");

    var url = "http://127.0.0.1:5000/predict_home_prices";
    $.post(url,{
        city: city.value,
        bedroom: parseFloat(bedroom.value),
        bathroom: parseFloat(bathroom.value),
        sqft_living: parseFloat(living_area.value),
        sqft_lot: parseFloat(lot_area.value),
        floors: floors,
        view: view,
        condition: condition,
        sqft_basement: parseFloat(basement_area.value)
    },function(data, status){
        console.log(data.estimated_price);
        est_price.innerHTML = "<h2>" + "$ " + data.estimated_price.toString() + " </h2>";
        console.log(status);
    });
}



function OnPageLoad(){
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_city";
   // var url = "/api/get_city";
    $.get(url,function(data, status){
        console.log("got response for get_city request");
        if(data){
            var city= data.city;
            var uiCity= document.getElementById("uicity");
            $('#uicity').empty();
            for(var i in city){
                var opt = new Option(city[i]);
                $('#uicity').append(opt);
            }
        }
    });
}


window.onload = OnPageLoad;