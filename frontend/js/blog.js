
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

        containner.innerHTML+="<div class='containner border p-4 mt-3 bg-light rounded '>"+marked(data)+"</div>"
        console.log(marked(data))
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