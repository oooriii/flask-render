<script>
import bet from './bet.vue'
import bets from './bets.vue'
  
export default {
  components: {
    bet,
    bets
  },
  data() {
    return {
      prova: {
        camp: 'antonio'
      }
    }
  }
}
</script>

<template>
  <div class="demo">
    <!--
    	<bet :obj="prova"></bet>
   --> 
    <bets></bets>
  </div>
</template>