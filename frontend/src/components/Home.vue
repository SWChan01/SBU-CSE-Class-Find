<template>
  <div>
    <Searchbox v-on:searchquery="searchQuery" />
    <Classes v-bind:classList="classes" v-bind:classTimes="allsavedClassesTimes" />
  </div>
</template>

<script>
import Searchbox from "./Searchbox";
import allClasses from "../allClasses";
import Classes from "./Classes";
import axios from "axios"

export default {
  name: "App",
  components: {
    Searchbox,
    Classes,
  },

  data() {
    return {
      classes: allClasses,
      allsavedClassesTimes :{ 'M':[],'TU':[], 'W':[] , 'TH':[],'F':[] }
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

      else if(mode === "Day"){
        this.classes = allClasses.filter(
          element => element.days.includes(query)
        );
      }




      

    },



    convertTime12to24(time12h) {
      const [time, modifier] = time12h.split(' ');

      let [hours, minutes] = time.split(':');

      if (hours === '12') {
          hours = '00';
      }

      if (modifier === 'PM') {
          hours = parseInt(hours, 10) + 12;
      }

      return `${hours}:${minutes}`;
    },
  },
  mounted(){

    console.log("all saved class times AT HOME "+this.allsavedClassesTimes);

    axios
    .get("http://127.0.0.1:5000/scheduleOPS")
    .then(resp=>{
        console.log(JSON.parse(resp.data.result));
        let allsavedclasses = JSON.parse(resp.data.result);

        allsavedclasses.forEach(element => {


            //convert time to minutes format

            let startTime = this.convertTime12to24(element.startTime);
            let endTime = this.convertTime12to24(element.endTime);

            let startTimeHour = parseInt(startTime.substring(0,2));
            let startTimeMinute = parseInt(startTime.substring(3,5));

            let endTimeHour = parseInt(endTime.substring(0,2));
            let endTimeMinute = parseInt(endTime.substring(3,5));


            let convertedStart = startTimeHour * 60 + startTimeMinute;
            let convertedEnd = endTimeHour * 60 +endTimeMinute;
            

            

            

            for(let i =0;i<element.days.length;i++){
              if(element.days.charAt(i) === "T"){
                this.allsavedClassesTimes[element.days.substring(i,i+2)].push([convertedStart,convertedEnd]);
                i++;
              }
              
              else if(element.days.charAt(i) === "M" || element.days.charAt(i) === "F" || element.days.charAt(i) === "W"   ){
                this.allsavedClassesTimes[element.days.charAt(i)].push([convertedStart,convertedEnd]);
              }


              else{
                if(element.days === "RECM") this.allsavedClassesTimes["M"].push([convertedStart,convertedEnd]);

                if(element.days === "RETU") this.allsavedClassesTimes["TU"].push([convertedStart,convertedEnd]);

                if(element.days === "RECW") this.allsavedClassesTimes["W"].push([convertedStart,convertedEnd]);

                if(element.days === "RETH") this.allsavedClassesTimes["TH"].push([convertedStart,convertedEnd]);

                if(element.days === "RECF") this.allsavedClassesTimes["F"].push([convertedStart,convertedEnd]);

                i+=100;
              }



            }


        });


        console.log("all saved class times AT HOME 2 : "+this.allsavedClassesTimes);





    })
  },




};
</script>

<style>

</style>