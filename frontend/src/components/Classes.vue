<template>
<div>
    <ol>
        <li v-bind:key="eachClass.id" v-for = "eachClass in classList">
            <ClassItem v-bind:eachClass ="eachClass" v-bind:classTimes="classTimes"  />
        </li>
    </ol>
</div>
</template>

<script>

import ClassItem from './ClassItem'


export default {
    name : "Classes",
    components :{
        ClassItem,
    },

    props : ["classList","classTimes"],





}
</script>

<style scoped>
</style>