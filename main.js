var vm = new Vue({
         el: '#vue-app',
         data: {

                 books: [
                   '888',
                   'bet365',
                   'bwin',
                   'WilliamHill',
                   'Codere',
                   'marcaapuestas',
                   'paf',
                   'marathon bet',
                   'retabet.es',
                   'Gran Casino Madrid',
                   'Casino Barcelona',
                   'Winamax',
                   'BetFred',
                   'Mr Green',
                   'sportium',
                   'Wanabet',
                   'star vegas',
                   'LeoVegas',
                   'Juegging',
                   '777',
                   'Versus',
                   'betfair sportbook',
                 ],
                 bookies: {
                  '1':'888',
                  '2':'bet365',
                  '7':'bwin',
                  '20':'WilliamHill',
                  '39':'Codere',
                  '45':'marcaapuestas',
                  '46':'paf',
                  '55':'marathon bet',
                  '57':'retabet.es',
                  '61':'Gran Casino Madrid',
                  '62':'Casino Barcelona',
                  '69':'Winamax',
                  '70':'BetFred',
                  '72':'Mr Green',
                  '48':'sportium',
                  '52':'Wanabet',
                  '54':'star vegas',
                  '71':'LeoVegas',
                  '76':'Juegging',
                  '75':'777',
                  '65':'Versus',
                  '4':'betfair sportbook',
                 },
                 sports:{
                   '1': 'Futbol',
                   '2': 'Tennis',
                 },
                 results: null,
                 offset: 0,
                 count: 0,
                 bet_type: 'normal',
                 name:'sportium',
                 message: {
                         missatge: '',
                         status: '',
                 },
         },
         methods:{
                 get_odds: function(){
                  this.loading=true;
                  self=this;

                  //axios.get('/get_odds/'+self.name).

                  data = {offset: this.offset, bet_type: this.bet_type};
                  axios.post('/get_odds/'+self.name, data).
                  then(function(response){
                        //self.results = JSON.parse(response.data);
                        //self.results = response.data.json();
                        console.log(response.data);
                        self.results = response.data.data;
                        self.count = parseInt(response.data.allEventsCount);
                        self.offset = parseInt(response.data.offset);
                  }).
                  //catch(response => (this.message =  JSON.parse(response.data) )).
                  finally(function(){
                         self.loading=false;
                  });


                 },
                 next: function(){
                   this.offset += 10;
                   this.get_odds();
                 },
                 prev: function(){
                   this.offset -= 10;
                   this.get_odds();
                 }

               },

              mounted () {

              },

      });

