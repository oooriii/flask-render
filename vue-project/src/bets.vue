<template>
  <div>
      <bet :obj="obj"></bet>
      <pre>
            {{ obj }}
      </pre>

  </div>
</template>

<script>
import bet from './bet.vue'
export default {
  name: 'bets',
  components:{
    bet,
},
  data() {
    return {
        obj: {
          camp: 'paco',
        }

    }


  },

}

</script>
