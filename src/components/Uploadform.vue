<template>
  <div class="container col-md-8">
    <form action="" method="post" enctype="multipart/form-data" @submit.prevent="uploadPhoto">

      <!-- description -->
      <div class="fom-group pb-3">
        <label for="description" class="col-sm-2 col-form-label">
          Description <span class="text-danger">(Required)</span>
        </label>
        <div class="col-sm-10">
            <textarea name="description" id="" cols="30" rows="10"></textarea>
        </div>
      </div>

      <!-- photo -->
        <div class="fom-group pb-3">
            <label for="photo" class="col-sm-2 col-form-label">
                Photo Upload: <span class="text-danger">(Required)</span>
            </label>
            <div class="col-sm-10">
                <input type="file" name="photo">
            </div>
        </div>
        
        <button type="submit info" class="btn btn-info">Add Image</button>
    </form>
  </div>
</template>

<script>
export default {
  data(){
      return {}
  },
  methods:{
      uploadPhoto(){
          fetch('/api/upload',{
              method: 'POST'
          }).then((response)=>{
              return response.json();
          }).then((data)=>{
              console.log(data);
          }).catch((error)=>{
              console.log(error);
          });
      }
  },
};
</script>