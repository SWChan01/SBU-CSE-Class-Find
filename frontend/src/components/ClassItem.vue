<template>
    <div class="class">
        {{eachClass.subj}} {{eachClass.course}}
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
            console.log(this.eachClass)
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
            }).catch((err)=>{
                console.log(err)
            })
        }
    }
}
</script>

<style >
    .class{
        border: 1px solid black;
        border-bottom: none;
        padding: 5px;
    }


    .add{
        margin-left: 80vw;
        padding: 20px;
        background-color:aquamarine;
    }

</style>