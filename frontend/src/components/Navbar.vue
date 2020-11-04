<template>
    <ul>
        <li> <router-link to="/">  <a>Search for classes</a>   </router-link></li>
        <li> <router-link to="/schedule"> <a>View Schedule</a>  </router-link></li>
    </ul>
</template>

<script>
export default {

}
</script>

<style >


ul{
    height: 50px;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;

}


ul li {
    float: left;
    margin-left: 25vw;
}

a{
    display: block;
    text-decoration: none;
    color: white;
    padding: 8px;
    font-size: 20px;

}

a:hover{
    background-color: #111;
}






</style>