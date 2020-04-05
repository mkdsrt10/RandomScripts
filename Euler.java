import java.util.*;
// import java.io.BufferedReader;
// import java.io.FileReader;
// import java.io.IOException;
//
// import java.io.File;
// import java.io.FileWriter;

public class Euler{
  public static String backwardEuler(float dt){
    float x = 1;
    float v = 0;
    float t = 0;
    String w = "";
    w += x+"\n";
    // System.out.print(x);
    while(t<=5){
      t += dt;
      float xNew = ((v*dt)+x*(1+(dt/2)))/(1+(dt/2)+(10*dt*dt));
      float vNew = (v-(10*dt*x))/(1+(dt/2)+(10*dt*dt));
      x = xNew;
      v = vNew;
      w += x+"\n";
      // System.out.print(", "+x);
    }
    return w;
  }
  public static String forwardEuler(float dt){
    float x = 1;
    float v = 0;
    float t = 0;
    String w = "";
    // System.out.print(x);
    w+=x+"\n";
    while(t<=5){
      t += dt;
      float xNew = x+(v*dt);
      float vNew = v-(10*x*dt)-(v*dt/2);
      x = xNew;
      v = vNew;
      // System.out.print(", "+x);
      w+=x+"\n";
    }
    return w;
  }
  public static void main(String[] str){
    Scanner sc = new Scanner(System.in);
    float dt = sc.nextFloat();
    // System.out.println("Forward Euler :");
    // forwardEuler(dt);
    // System.out.println("\nBackward Euler :");
    // backwardEuler(dt);
    // System.out.println("");

    try{
      // String Lr = backwardEuler(dt);
      float t =0;
      FileWriter fw=new FileWriter("TIME.txt");
      while(t<=5){
        fw.write(t+"\n");
        t+=dt;
        // System.out.println("asfdgcv");
      }
      fw.close();
    }
    catch(IOException e){
      e.printStackTrace();
    }

    try{
      String Lr = backwardEuler(dt);
      FileWriter fw=new FileWriter("backwardPlot.txt");
      fw.write(Lr);
      fw.close();
    }
    catch(IOException e){
      e.printStackTrace();
    }

    try{
      String Lr = forwardEuler(dt);
      FileWriter fw=new FileWriter("forwardPlots.txt");
      fw.write(Lr);
      fw.close();
    }
    catch(IOException e){
      e.printStackTrace();
    }
  }
}
