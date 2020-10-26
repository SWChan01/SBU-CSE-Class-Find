<template>
  <div>
    <Searchbox v-on:searchquery="searchQuery" />
    <Classes v-bind:classList="classes" />
  </div>
</template>

<script>
import Searchbox from "./Searchbox";
import allClasses from "../allClasses";
import Classes from "./Classes";
import axios from 'axios';



export default {
  name: "App",
  components: {
    Searchbox,
    Classes,
  },

  data() {
    return {
      classes: allClasses,
    };
  },

  methods: {
    searchQuery(query) {
      console.log(query);
    
      //let courseName = query.substring(0,3);
      let courseNum = query.substring(3, 6);

      console.log(courseNum);

      console.log(allClasses);

      this.classes = this.classes.filter(
        (element) => element.course == courseNum
      );


      axios
        .get("http://127.0.0.1:5000/hello")
        .then(resp=>{
          console.log(resp.data);
        })




    },  
  },
};
</script>

<style>

</style>