<template>
  <div class="container col-md-8">
    <form action="" method="post" id="uploadForm"  @submit.prevent="uploadPhoto">

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
      return {
        csrf_token: ''
      }
  },
  created(){
          this.getCsrfToken();
        },
  methods:{
       
      uploadPhoto(){
          let uploadForm = document.getElementById('uploadForm');
          let form_data = new FormData(uploadForm);

          fetch('/api/upload',{
              method: 'POST',
              body: form_data,
              headers: {
                    'X-CSRFToken': this.csrf_token
                    }
          })
          .then((response)=>{
              return response.json();
          })
          .then((data)=>{
              console.log(data);
          })
          .catch((error)=>{
              console.log(error);
          });
      },
      getCsrfToken(){
          let self =this;
          fetch('/api/csrf-token')
          .then(response=>
              response.json())          
          .then(data=>{
            self.csrf_token = data.csrf_token;
          })

      }
  },
};
</script>