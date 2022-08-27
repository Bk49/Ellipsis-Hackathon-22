<script>
    import NavBar from './components/navigations/NavBar.vue';
    export default {
    name : 'App',
    components: {
        NavBar,
    }
    }
</script>

<template>
    <div id="app">
        <nav-bar></nav-bar>
        <router-view></router-view>
    </div>
</template>

<style scoped>
</style>
