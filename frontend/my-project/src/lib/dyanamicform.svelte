<script>
    let data=[
  {
    "name": "title",
    "label": "Book Title",
    "type": "text",
    "placeholder": "Enter book title"
  },
  {
    "name": "author",
    "label": "Author Name",
    "type": "text",
    "placeholder": "Enter author name"
  },
  {
    "name": "published_date",
    "label": "Published Date",
    "type": "date"
  },
  {
    "name": "price",
    "label": "Price",
    "type": "number",
    "min": 1,
    "max": 1000,
    "placeholder": "Enter price"
  },
  {
    "name": "categories",
    "label": "Category",
    "type": "select",
    "options": ["Fiction", "Non-Fiction", "Mystery", "Fantasy", "Biography"]
  },
  {
    "name": "description",
    "label": "Description",
    "type": "textarea",
    "placeholder": "Enter book description"
  },
  {
    "name": "isbn",
    "label": "ISBN",
    "type": "text",
    "placeholder": "Enter ISBN number"
  },
  {
    "name": "stock",
    "label": "Stock",
    "type": "number",
    "min": 1,
    "max": 500,
    "placeholder": "Enter stock quantity"
  },
  {
    "name": "submit",
    "label": "Submit",
    "type": "button"
  }
]

</script>
<div>
    <form>
        {#each data as item }
        {#if item.type=="select"}
             <label>{item.label}</label>
             <select>
                <option name={item.name}>select by {item.label}</option>
                {#each item.options as option}
                <option value={option}>{option}</option>
                {/each}
             </select>
        {:else if item.type=="button"}
            <button>{item.label}</button>
            
        {:else}
             {#if item.type=="textarea"}
             <label>{item.label}</label>
             <textarea name={item.name} placeholder={item.placeholder}></textarea>
             {:else if item.type=="text"}
                 <label>{item.label}</label>
                <input type={item.type} name={item.name} placeholder={item.placeholder} />
             {:else}
               <label>{item.label}</label>
                <input type={item.type} name={item.name} placeholder={item.placeholder} min={item.min} max={item.max} />
             {/if}
                
        {/if}
            
        {/each}
    </form>
</div>