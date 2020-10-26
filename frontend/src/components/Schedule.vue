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
            <td class="selected">CSE 303 (1:15PM-2:35pm) <p>Introduction To Theory Of Computations</p></td>
            <td></td>
            <td class="selected">CSE 303 (1:15PM-2:35pm) <p>Introduction To Theory Of Computations</p></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>2:00pm</td>


            <td></td>
            <td class="selected">CSE 303 (1:15PM-2:35pm) <p>Introduction To Theory Of Computations</p></td>
            <td></td>
            <td class="selected">CSE 303 (1:15PM-2:35pm) <p>Introduction To Theory Of Computations</p></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>3:00pm</td>


            <td></td>
            <td class="selected">CSE 373 (3:00PM-4:20PM) <p>Analysis Of Algorithms</p></td>
            <td></td>
            <td class="selected">CSE 373 (3:00PM-4:20PM) <p>Analysis Of Algorithms</p></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>4:00pm</td>


            <td class="selected">CSE 312 (4:25PM - 5:45PM) <p>Legal, Social, and Ethical Issues in Information Systems</p></td>
            <td class="overlap">CSE 373 (3:00PM-4:20PM) <p>Analysis Of Algorithms</p><br>CSE 316 (4:45PM - 6:05PM) <p>Fundamentals Of Software Development</p></td>
            <td class="selected">CSE 312 (4:25PM - 5:45PM) <p>Legal, Social, and Ethical Issues in Information Systems</p></td>
            <td class="overlap">CSE 373 (3:00PM-4:20PM) <p>Analysis Of Algorithms</p><br>CSE 316 (4:45PM - 6:05PM) <p>Fundamentals Of Software Development</p></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>5:00pm</td>



            <td class="selected">CSE 312 (4:25PM - 5:45PM) <p>Legal, Social, and Ethical Issues in Information Systems</p></td>
            <td class="selected">CSE 316 (4:45PM - 6:05PM) <p>Fundamentals Of Software Development</p></td>
            <td class="selected">CSE 312 (4:25PM - 5:45PM)<p>Legal, Social, and Ethical Issues in Information Systems</p></td>
            <td class="selected">CSE 316 (4:45PM - 6:05PM) <p>Fundamentals Of Software Development</p></td>
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
                let startTime = this.convertTime12to24(element.startTime)
            
            


                for(let i=0;i<allDays.length;i++){
                    let day = allDays.charAt(i);
                    
                    console.log("day: "+day +" , start time :"+startTime);



                    if(day === 'T'){
                        let daySelector = this.daysDict[allDays.substring(i,i+2)];
                        i++;

                        let startTimeSelector = this.timeDict[startTime.substring(0,2)];

                        

                        console.log("day selector : "+daySelector +"start time selector :"+startTimeSelector);
                        let targetDom = document.getElementsByTagName("tr")[startTimeSelector+1].childNodes[daySelector+1];
                        targetDom.classList.add("selected");
                        targetDom.innerHTML = `${element.subj} ${element.course} (${element.startTime}-${element.endTime}) <p> ${element.courseName} </p>`;
                    }


                    else if (day === 'R'){
                        let daySelector = this.RecDayDict[allDays];
                        let startTimeSelector = this.timeDict[startTime.substring(0,2)];
                        i+=4;
                        console.log("day selector :" + daySelector+" start time: "+startTimeSelector);

                        let targetDom = document.getElementsByTagName("tr")[startTimeSelector+1].childNodes[daySelector+1];
                        targetDom.classList.add("selected");
                        targetDom.innerHTML = `${element.subj} ${element.course} (${element.startTime}-${element.endTime}) <p> ${element.courseName} </p>`;
                    }


                    else{
                        let daySelector = this.daysDict[day];
                        let startTimeSelector = this.timeDict[startTime.substring(0,2)];

                        console.log("day selector :" + daySelector+" start time: "+startTimeSelector);

                        let targetDom = document.getElementsByTagName("tr")[startTimeSelector+1].childNodes[daySelector+1];
                        targetDom.classList.add("selected");
                        targetDom.innerHTML = `${element.subj} ${element.course} (${element.startTime}-${element.endTime}) <p> ${element.courseName} </p>`;




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
    }

    td{
        padding-bottom: 10px;
        padding-right:30px ;
        border-right: 1px solid black;
        height: 50px;
        word-wrap: break-word;         /* All browsers since IE 5.5+ */
        overflow-wrap: break-word;
    }

    tr{
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