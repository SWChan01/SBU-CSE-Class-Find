<template>
    <div class="class">
        {{eachClass.subj}} {{eachClass.course}}
        <button class="add">Add</button>
    </div>
</template>

<script>



export default {
    name : "ClassItem",
    props: ["eachClass"],
}
</script>

<style>
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