<template>
    <div class="class">

  
            <div class="span1 heading">
                <p>{{eachClass.subj}}{{eachClass.course}}.{{eachClass.section}}</p> 
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
    props: ["eachClass"],



// subj:all_courses[i][0],
//             course:all_courses[i][1],
//             component:all_courses[i][2],
//             section:all_courses[i][3],
//             days:all_courses[i][4],
//             startTime:all_courses[i][5],
//             endTime:all_courses[i][6],
//             startDate:all_courses[i][7],
//             endDate:all_courses[i][8],
//             duration:all_courses[i][9],
//             instructionMode:all_courses[i][10],
//             building:all_courses[i][11],
//             room:all_courses[i][12],
//             instructor:all_courses[i][13],
//             enrollmentCap:all_courses[i][14],
//             waitCap:all_courses[i][15],
//             combinedSession:all_courses[i][16],
//             combinedSessionCap:all_courses[i][17],


    methods: {
        saveClass(){
            console.log(this.eachClass);


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



        },

        // checkOverlapping(A){
        //     A.sort((a, b) => a[1] - b[1]); // Sort by end time
        //     for (let i = 0; i < A.length; ++i) {
        //         const end = A[i][1];
        //         if (A[i + 1] && A[i + 1][0] < end) { 
        //             return false;
        //         }
        //     }
        //     return true;

        // }




    }
}
</script>

<style >
    .class{
        border: 1px solid black;
        border-bottom: none;
        padding: 5px;
        position: relative;
    }


    .add{
        position: absolute;
        background-color:aquamarine;
        top: 70px;
        left: 70vw;
        padding: 10px;
    }

    .span1{
        display: inline-block;
    }
    .courseInfo{
        margin-left:20vw;
        margin-top:2vw;

    }
</style>