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
                this.allsavedclasses = JSON.parse(resp.data.result);
            })
        },

        assignAttr(){
            this.allsavedclasses.forEach(element => {
                
                let allDays = element.days;
                let startTime = this.convertTime12to24(element.startTime);


                let daySelector;
                let startTimeSelector;
            
        
                for(let i=0;i<allDays.length;i++){
                    let day = allDays.charAt(i);



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

            
                    let targetDom = document.getElementsByTagName("tr")[startTimeSelector+1].childNodes[daySelector+1];
                    let secondDom = document.getElementsByTagName("tr")[startTimeSelector+2].childNodes[daySelector+1];
                    let thirdDom;
                    let fourthDom;

                    if(document.getElementsByTagName("tr")[startTimeSelector+4])
                        thirdDom = document.getElementsByTagName("tr")[startTimeSelector+3].childNodes[daySelector+1];
                    if(document.getElementsByTagName("tr")[startTimeSelector+4])
                        fourthDom = document.getElementsByTagName("tr")[startTimeSelector+4].childNodes[daySelector+1]

                    let minute = element.startTime.substring(3,5);
                    let res = parseInt(minute) +parseInt(element.duration);

                    console.log("min "+minute+" res "+res)

                    
                    //if the class takes up two hour slots
                    if(res>60){

                        if(res<120){

                            this.insertClass(targetDom,element,true);
                            this.insertClass(secondDom,element,false);
                            targetDom.classList.add("twoClass");
                        }

                        else if(res<180){
                            this.insertClass(targetDom,element,true);
                            this.insertClass(secondDom,element,false);
                            this.insertClass(thirdDom,element,true);
                            targetDom.classList.add("twoClass");
                        }

                        else{
                            this.insertClass(targetDom,element,true);
                            this.insertClass(secondDom,element,false);
                            this.insertClass(thirdDom,element,true);
                            this.insertClass(fourthDom,element,true);
                            targetDom.classList.add("twoClass");
                            secondDom.classList.add("twoClass");
                            thirdDom.classList.add("twoClass");
                        }


                    
                    }


                    else{
                        //targetDom.innerHTML = `${element.subj} ${element.course} (${element.startTime}-${element.endTime}) <p> ${element.courseName} </p>`;
                        this.insertClass(targetDom,element,true);
                    }

                    

                
                }



            })
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
                
                destDOM.classList.add("overlap")
                
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
        border-right: 1px solid rgb(202, 189, 189);
        height: 50px;
        word-wrap: break-word;         /* All browsers since IE 5.5+ */
        overflow-wrap: break-word;
        border-bottom: 1px solid  rgb(206, 186, 186);
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
        background-color:bisque
    }

    .overlap{
        background-color:violet
    }

    .twoClass{
        border-bottom: none;
    }
</style>