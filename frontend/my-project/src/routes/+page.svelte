<script>
	import Model from './../../lib/model.svelte';
    import { goto } from "$app/navigation";
    import axios from "axios";
    import { onMount } from "svelte";
  import { validateAutorName, validatebook, validateDate, validatePrice } from '$lib';

  let title=""
  let author=""
  let published_date=""
  let price=""
  let token=""
  let Alertmassage=""
  let warn=false
let showAlert=false
const closeAlert=()=>{
    showAlert=false
}
  const handelAdd=()=>{
    if(title==""|| author==""||published_date==""||price==""){
      showAlert=true
      warn=true
      Alertmassage="Please fill all the fields"
      
    }
    else{
      if(validateAutorName(author)&&validateDate(published_date)&& validatePrice(price)&& validatebook(title)){
        
    let book={  
        title:title,
        author:author,
        published_date:published_date,
        price:Number(price)
        }
     axios.post("http://127.0.0.1:8000/api/books/",book,
     {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
            }
    }
     )
     .then((response)=>{
        console.log(response.data)
         showAlert=true
         Alertmassage="Book Added Successfully"
        goto("/")
     })
     .catch((error)=>{  
        console.log(error)
      })
      }}
  }
  onMount(()=>{
    token = localStorage.getItem("token") ?? "";
    console.log("Token loaded:", token);
  })
</script>
<div>
    <div class="w-full p-3 text-center">
        <h1 class=" text-3xl font-bold">Add Book Information</h1>
    </div>
    <div class="lg:w-5/12 md:w-7/12 sm:w-10/12 p-3.5 m-auto mt-5 ">

        
        <label  >Book Name    </label>
        <input placeholder="book name" type="text" bind:value={title} class=" w-full border-b-2  p-0.5 pl-2  mb-2 mt-2 outline-0  focus:border-red-600"/>
        
        {#if title!=""&&!validatebook(title)}
            <p class="text-center text-red-600  animate-pulse">Name must be +2 letters and contain alphabets</p>
         {/if}
         
        <label>Author Name</label>
        <input placeholder="author name" type="text" bind:value={author} class=" w-full border-b-2  p-0.5 pl-2  mb-2 mt-2 outline-0 focus:border-red-600"/>
        {#if author!=="" &&!validateAutorName(author)}
            <p class="text-center text-red-600  animate-pulse">Name must be +2 letters and contain alphabets</p>
         {/if}
        <label>Published Date</label>
        <input placeholder="book published_date" type="date" bind:value={published_date} class=" w-full border-b-2  p-0.5 pl-2  mb-2 mt-2 outline-0 focus:border-red-600"/>
        {#if published_date!=="" &&!validateDate(published_date)}
         
              <p class="text-red-600 animate-pulse">Invalid Date</p>
            
        {/if}
        <label>Price</label>
        <input placeholder="book price" min="1" type="number" bind:value={price} class=" w-full border-b-2  p-0.5 pl-2  mb-2 mt-2 outline-0 focus:border-red-600" />
        {#if price!==""&&!validatePrice(price)}
             <p class="text-center text-red-600  animate-pulse">Price must be greater than 0</p>
          {/if}
        <button class=" w-full mt-5 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-xl" on:click={handelAdd} >Add Book</button>
    </div>
    <Model isOpen={showAlert} message={Alertmassage} onClose={closeAlert} warning={warn}/>
</div>
