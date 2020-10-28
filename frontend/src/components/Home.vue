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

export default {
  name: "App",
  components: {
    Searchbox,
    Classes,
  },

  data() {
    return {
      classes: allClasses,
      allsavedClassesTimes : [],
    };
  },

  methods: {
    searchQuery(query,mode) {
      console.log(query);
      console.log("mode is "+mode);
    
      //let courseName = query.substring(0,3);
      let courseNum = query.substring(3, 6);

      console.log(courseNum);

      console.log(allClasses);

      console.log("ertguihgerigerierg"+allClasses[0].courseName)

      if(mode === "All Fields"){
          this.classes = allClasses.filter(
            element => {
              element.course.includes(query)
            }
        );
      }

      else if(mode === "Time"){
        this.classes = allClasses.filter(
          element => element.startTime.includes(query)
        );
      }
      else if(mode === "Title"){
        this.classes = allClasses.filter(
          element => element.courseName.includes(query)
        );
      }

      else if(mode === "Class Number"){
        this.classes = allClasses.filter(
          element => element.course.includes(query)
        );
      }




      

    },

    //  getData(){
    //         return axios
    //         .get("http://127.0.0.1:5000/scheduleOPS")
    //         .then(resp=>{
    //             console.log(JSON.parse(resp.data.result));
    //             this.allsavedclasses = JSON.parse(resp.data.result);
    //         })
    //     },
    

    



  },
};
</script>

<style>

</style>