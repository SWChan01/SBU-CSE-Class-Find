<template>
    <form @submit.prevent = "$emit('searchquery',query,mode)">

        <input v-model="query" type="text">

        <select name="option" id="option" v-model="mode">
            <option value="All Fields">All Fields</option>
            <option value="Title">Title</option>
            <option value="Class Number">Class Number</option>
            <option value="Day">Day</option>
            <option value="Time">Time</option>
        </select>


        <button class="submitBtn">Submit</button>

    </form>
</template>

<script>
export default {
    name: "Searchbox",


    data() {
        return {
            query: "",
            mode:"All Fields",
        }
    },
}
</script>

<style>
    input{
        margin-left: 15vw;
        width:50vw;
        padding: 5px;
    }
    
    .submitBtn{
        margin-left: 10px;
        padding: 5px;
    }
    form{
        display: inline-block;
    }


    select{
        padding: 5px;
        margin-left: 10px;
    }
</style>