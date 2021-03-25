let a = document.getElementById('loginbtn');
a.addEventListener("click",clickbtn);

function clickbtn(){
    console.log("function buttonclick")
    const xhr =new XMLHttpRequest();
    xhr.open('GET','login',true);
    xhr.onprogress = function()
    {
        console.log("loading");
    }
    
    xhr.onload=function()
    {
        if(this.status ===200)
            {
                
                document.querySelector("#main1").innerHTML = this.responseText;
            }
        else
            {
                console.log("some error occure")
            }
        
    }
    xhr.send();
    
}
let b= document.getElementById('sub');
b.addEventListener("click",subm);
function subm(){
    console.log("this is submit")
}