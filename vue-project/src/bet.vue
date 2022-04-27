<template>
  <div>
      <h1>{{ obj.camp }}</h1>
      <button @click="do_more">click</button>
  </div>
</template>

<script>
export default {
  name: 'bet',
  props: {
    obj: Object
  },
  methods:{
    do_more: function(){
      this.obj['camp'] = 'manolo';
    },
  }




}

</script>
