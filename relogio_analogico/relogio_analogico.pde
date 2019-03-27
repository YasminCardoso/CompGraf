void setup(){
  size(600,600);
  ellipseMode(CENTER);
}
void draw(){
  background(200);
  translate(width/2,height/2);
  float raio = 0.45*width;
  fill(255);
  strokeWeight(6);
  ellipse(0,0,2*raio,2*raio);
  
  int s = second();
  float m = minute()+s/60.0;
  float h = hour()+m/60.0;
  
  beginShape();
  
  float teta = (TWO_PI*s/60)-HALF_PI;
  float tetam = (TWO_PI*m/60)-HALF_PI;
  float tetah = (TWO_PI*h/12)-HALF_PI;
  line(0,0,raio*cos(tetam)*0.75,raio*sin(tetam)*0.75);
  strokeWeight(8);
  line(0,0,raio*cos(tetah)*0.65,raio*sin(tetah)*0.65);
  fill(230,40,40);
  stroke(230,40,40);
  ellipse(0,0,10.0,10.0);
  strokeWeight(4);
  line(0,0,raio*cos(teta)*0.75,raio*sin(teta)*0.75);
  stroke(0);
  for(int i=0; i<60; i++){
      strokeWeight(2);
      line(raio*cos(TWO_PI*i/60)*0.95,raio*sin(TWO_PI*i/60)*0.95,raio*cos(TWO_PI*i/60),raio*sin(TWO_PI*i/60));
      if(i%5 == 0){
        strokeWeight(3);
        line(raio*cos(TWO_PI*i/60)*0.90,raio*sin(TWO_PI*i/60)*0.90,raio*cos(TWO_PI*i/60),raio*sin(TWO_PI*i/60));
        strokeWeight(2);
      }
    }
    endShape();
}
