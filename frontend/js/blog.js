
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
        var clon = document.getElementsByTagName("template")[0].content.cloneNode(true);
        clon.getElementById('content').innerHTML=marked(data);
        clon.getElementById('name').innerHTML="blog";
        containner.appendChild(clon)
        console.log("containner. "+containner)
        deleteBtn=document.getElementById("delete")
        if(deleteBtn)
        {
            console.log("btn "+deleteBtn)
            deleteBtn.addEventListener("click", function(){DeletePost(path)})
            deleteBtn.id=''
        }

        // containner.innerHTML+="<div class='containner border p-4 mt-3 bg-light rounded '>"+marked(data)+"</div>"
        console.log(marked(data))
        // alert("Data: " + data + "\nStatus: " + status);
    });
}
function DeletePost(id)
{
    $.post( "/delpost", {
        javascript_data: id,
        contentType: "application/json; charset=utf-8", // this
        dataType: "json", // and this
    });
    location.reload();
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