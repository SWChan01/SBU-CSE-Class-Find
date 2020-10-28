<template>

<div>
    <h4>Name:Singwa Chan</h4>
    <h4>ID:112305543</h4>

    <table>
        <tr>
            <th>Time</th>
            <th>Monday</th>
            <th>Tuesday</th>
            <th>Wednesday</th>
            <th>Thursday</th>
            <th>Friday</th>
            <th>Saturday</th>
            <th>Sunday</th>  
        </tr>

        <tr>
            <td>8:00am</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>

        <tr>
            <td>9:00am</td>


            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>10:00am</td>


            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>11:00am</td>


            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>12:00pm</td>


            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>1:00pm</td>


            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>2:00pm</td>


            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>3:00pm</td>


            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>4:00pm</td>


            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>5:00pm</td>



            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>6:00pm</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>7:00pm</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>8:00pm</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>



    </table>
</div>
   
</template>

<script>
import axios from 'axios'

export default {


    data(){
        return{
            allsavedclasses : [],
            classAttr : [],
            daysDict : {'M':0,'TU':1,'W':2,'TH':3,'F':4},
            RecDayDict:{'RECM':0,'RETU':1,'RECW':2,'RETH':3,'RECF':4}
            ,
            timeDict : {'08':0,'09':1,'10':2,'11':3,'12':4,'13':5,'14':6,'15':7,'16':8,'17':9,'18':10,'19':11,'20':12,'21':13},
        }
    },


    methods : {


        getData(){
            
            return axios
            .get("http://127.0.0.1:5000/scheduleOPS")
            .then(resp=>{
                console.log(JSON.parse(resp.data.result));
                this.allsavedclasses = JSON.parse(resp.data.result);
            })
        },

        assignAttr(){
            console.log(this.allsavedclasses);
            this.allsavedclasses.forEach(element => {
                
                let allDays = element.days;
                let startTime = this.convertTime12to24(element.startTime);


                let daySelector;
                let startTimeSelector;
            
        
                for(let i=0;i<allDays.length;i++){
                    let day = allDays.charAt(i);
                    
                    console.log("day: "+day +" , start time :"+startTime);



                    if(day === 'T'){
                        daySelector = this.daysDict[allDays.substring(i,i+2)];
                        startTimeSelector = this.timeDict[startTime.substring(0,2)];
                        i++;   
                    }


                    else if (day === 'R'){
                        daySelector = this.RecDayDict[allDays];
                        startTimeSelector = this.timeDict[startTime.substring(0,2)];
                        i+=4;
                    }


                    else{
                        daySelector = this.daysDict[day];
                        startTimeSelector = this.timeDict[startTime.substring(0,2)];
                    }

                    console.log("day selector : "+daySelector +"start time selector :"+startTimeSelector);
                    let targetDom = document.getElementsByTagName("tr")[startTimeSelector+1].childNodes[daySelector+1];
                    let secondDom = document.getElementsByTagName("tr")[startTimeSelector+2].childNodes[daySelector+1];
                    

                    let minute = element.startTime.substring(3,5);
                    let res = parseInt(minute)
                    
                    //if the class takes up two hour slots
                    if(res+element.duration > 60){

                        // secondDom.classList.add("selected")
                        
                        // //separate contents acorss two hour slots
                        // targetDom.innerHTML = `${element.subj} ${element.course} (${element.startTime}-${element.endTime})`;
                        // secondDom.innerHTML = `<p> ${element.courseName} </p>`;
                        
                        // //get rid of bottom border
                        // targetDom.style = 'border-bottom:none'


                        this.insertClass(targetDom,element,true);
                        this.insertClass(secondDom,element,false);
                    
                    }


                    else{
                        //targetDom.innerHTML = `${element.subj} ${element.course} (${element.startTime}-${element.endTime}) <p> ${element.courseName} </p>`;
                        this.insertClass(targetDom,element,true);
                    }

                    

                
                }



            })
        },
        
        displayClasses(){
            console.log(this.allsavedclasses);
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

        insertClass (destDOM,element,isFirst){
            

            //if occupied
            if(destDOM.innerHTML){
                if(isFirst){
                    destDOM.innerHTML+=`<p>${element.subj} ${element.course}.${element.section}</p> <p>(${element.startTime}-${element.endTime})</p>`;
                }
                    
                else{
                    localStorage.temp = destDOM.innerHTML;
                    destDOM.innerHTML="";
                    destDOM.innerHTML+=`<p>${element.subj} ${element.course}.${element.section} (${element.startTime}-${element.endTime})</p>`;
                    destDOM.innerHTML+=localStorage.temp;
                } 
                
            }

            //when dom is not occupied
            else{

                destDOM.innerHTML+=`<p>${element.subj} ${element.course}.${element.section} (${element.startTime}-${element.endTime})</p>`;
                
    
            }


            destDOM.classList.add("selected");

        }



    },
    
    
    async mounted(){
        await this.getData();
        this.assignAttr();

    }

}
</script>

<style>
    table{
        border-collapse: collapse;
        width: 100%;
        table-layout: fixed;
        font-size: 11pt;
    }

    td{
        padding-bottom: 10px;
        padding-right:30px ;
        border-right: 1px solid black;
        height: 50px;
        word-wrap: break-word;         /* All browsers since IE 5.5+ */
        overflow-wrap: break-word;
        border-bottom: 1px solid black;
    }
/* 
    .days{
        padding-left: 30px;
        background-color: black;

    } */

    th{
        padding-left:30px;
        background-color:lightskyblue;
        color:black;
        height: 30px;
        padding-right:30px ;
    }

    .selected{
        background-color:gray
    }

    .overlap{
        background-color:mediumvioletred
    }
</style>