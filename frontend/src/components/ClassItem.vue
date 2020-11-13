<template>
    <div class="class">

  
            <div class="span1 heading">
                <p>{{eachClass.subj}}{{eachClass.course}}.{{eachClass.section}}</p>
                <br>
                <p>Building : {{eachClass.building}}</p>
                <p>Room: {{eachClass.room}}</p>
                <p>Enrollment Cap : {{eachClass.enrollmentCap}}</p>
                <p>Waitlist Cap: {{eachClass.waitCap}}</p>
                <p>Combined Description: {{eachClass.combinedSession}}</p>
                <p>Combined Enrollment Cap : {{eachClass.combinedSessionCap}}</p> 
            </div>
            <div class="span1 courseInfo">
                <p>{{eachClass.courseName}}</p>
                <p>Time: {{eachClass.days}} {{eachClass.startTime}}-{{eachClass.endTime}}</p>
                <p>Instructor:{{eachClass.instructor}}</p>
            </div>
      

       


       <button class="add" @click="saveClass">Add</button>

    </div>
</template>

<script>
import axios from 'axios'


export default {


    name : "ClassItem",
    props: ["eachClass","classTimes"],

    methods: {
        saveClass(){
            console.log(this.eachClass);
            
            //if no overlapping, save class



            //convert time to minutes format

            let startTime = this.convertTime12to24(this.eachClass.startTime);
            let endTime = this.convertTime12to24(this.eachClass.endTime);

            let startTimeHour = parseInt(startTime.substring(0,2));
            let startTimeMinute = parseInt(startTime.substring(3,5));


            let endTimeHour = parseInt(endTime.substring(0,2));
            let endTimeMinute = parseInt(endTime.substring(3,5));


            let convertedStart = startTimeHour * 60 + startTimeMinute;
            let convertedEnd = endTimeHour * 60 +endTimeMinute;


            // let temp = JSON.parse(JSON.stringify(this.classTimes));


            let temp = {'M':this.classTimes['M'],'TU':this.classTimes['TU'],'W':this.classTimes['W'],'TH':this.classTimes['TH'],'F':this.classTimes['F']};




            console.log(`TEMP 1:${temp['M']} tuesday:${temp['TU']} wednesday:${temp['W']} Thursday: ${temp['TH']} Friday:${temp['F']}`);

            for(let i =0;i<this.eachClass.days.length;i++){
                if(this.eachClass.days.charAt(i) === "T"){
                    temp[this.eachClass.days.substring(i,i+2)].push([convertedStart,convertedEnd]);
                    i++;
                }
            
                

                else if(this.eachClass.days.charAt(i) === "M" || this.eachClass.days.charAt(i) === "F" || this.eachClass.days.charAt(i) === "W"   ){
                    temp[this.eachClass.days.charAt(i)].push([convertedStart,convertedEnd]);
                }


                else{

                    if(this.eachClass.days == "RECM")
                        temp['M'].push([convertedStart,convertedEnd]);

                    else if(this.eachClass.days == "RETU") 
                        temp['TU'].push([convertedStart,convertedEnd]);

                    else if(this.eachClass.days == "RECW") 
                        temp['W'].push([convertedStart,convertedEnd]);

                    else if(this.eachClass.days == "RETH") 
                        temp['TH'].push([convertedStart,convertedEnd]);

                    else if(this.eachClass.days == "RECF") 
                        temp['F'].push([convertedStart,convertedEnd]);


                    i+=100;
                }


            }
        




            console.log(`TEMP 2  ${temp['M']} tuesday:${temp['TU']} wednesday:${temp['W']} Thursday: ${temp['TH']} Friday:${temp['F']}`);

            if(this.checkOverlapping(temp)){
                axios
                    .post("http://127.0.0.1:5000/scheduleOPS", {
                        subj : this.eachClass.subj,
                        course : this.eachClass.course,
                        section : this.eachClass.section,
                        days : this.eachClass.days,
                        startTime : this.eachClass.startTime,
                        endTime : this.eachClass.endTime,
                        duration : this.eachClass.duration,
                        room : this.eachClass.room,
                        courseName : this.eachClass.courseName,
                        
                    })
                    .then(() => {
                        console.log("saved");
                        this.$router.push('/schedule');
                    }).catch((err)=>{
                        console.log(err)
                    })
                    console.log("class times at classITEM:"+this.classTimes);
            }




            else{
                alert("there is schedule conflicts")
            }


            




        },

        checkOverlapping(A){

            for(let element in A){
                let arr = A[element];
                arr.sort((a, b) => a[1] - b[1]); // Sort by end time
                for (let i = 0; i < arr.length; ++i) {
                    const end = arr[i][1];
                    if (arr[i + 1] && arr[i + 1][0] < end) { 
                        return false;
                    }
                }
            }


            return true;


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





    }
}
</script>

<style >
    li{
        list-style-type: none;
    }
    .class{
        border: 1px solid rgb(185, 181, 181);
        border-bottom: none;
        padding: 5px;
        position: relative;
        width: 70%;
        margin-left: 15vw;
    }


    .add{
        position: absolute;
        background-color:aquamarine;
        top: 100px;
        left: 50vw;
        padding: 10px;
    }

    .span1{
        /* display: inline-block; */
        display:block;
    }
    .courseInfo{
        /* margin-left:35vw; */

        position: absolute;
        top: 75px;
        left: 20vw;

    }

    
</style>