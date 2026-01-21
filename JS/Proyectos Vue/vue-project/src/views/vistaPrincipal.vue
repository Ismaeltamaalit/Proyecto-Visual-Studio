<script setup>
import BarraLateral from '@/components/barraLateral.vue';
import barraLateral from '@/components/barraLateral.vue';

</script>

<template>
<div class="container">
    <BarraLateral> </BarraLateral>
    <div class="content">
        <router-view> </router-view>
    </div>
</div>
</template>

<style scoped>
.container{
    display: flex;
}
.content{
    flex: 1;
    padding: 20px;
}
</style>