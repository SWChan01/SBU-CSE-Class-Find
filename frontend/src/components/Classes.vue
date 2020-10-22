<template>
<div>
    <ol>
        <li v-bind:key="eachClass.id" v-for = "eachClass in classList">
            <ClassItem  v-bind:eachClass ="eachClass"  />
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

    props : ["classList"]
}
</script>

<style>
</style>