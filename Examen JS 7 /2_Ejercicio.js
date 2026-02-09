fetch('https://jsonplaceholder.typicode.com/posts/')
.then(response=>{
  if(!reesponse.ok)
    throw new Error("Error");
  return response.json();
})

.then(json=>{
  console.log(json.title +" - "+json.body);
})

.catch(error=>{
  console.error(error);
})
