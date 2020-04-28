
function Post()
{
    $.post( "/sendpost", {
        javascript_data: document.getElementById('comment-md').value,
        contentType: "application/json; charset=utf-8", // this
        dataType: "json", // and this
    });
    location.reload();
}

function GetPost(path)
{
    path=path.replace("\\", "/");
    console.log(path)

    containner=document.getElementById('postlist')
    $.get("/"+path,function(data, status){

        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        const page_type = urlParams.get('tag')
        data=JSON.parse(data)
        console.log(data)
        console.log(data["tags"])
        if(page_type==null||data["tags"].includes("#"+page_type)){
        console.log(data["str"])
        containner.innerHTML+="<div class='containner border p-4 mt-3 bg-light rounded '>"+marked(data["str"])+"</div>"
        console.log(data)

        console.log(marked(data["str"]))
        }
        // alert("Data: " + data + "\nStatus: " + status);
    });
}
function GetPosts()
{

    $.get("/getpost",function(data, status){
        data=JSON.parse(data)
        for(d of data.reverse())
        {
            GetPost(d)
        }
        // alert("Data: " + data + "\nStatus: " + status);
      
    
    });
}