import java.lang.*;

public class MultiThread extends Thread{
  public void run(){
    for(int i=0;i<5;i++){
      System.out.println(Thread.currentThread().getName()+"say hello"+i+"times");
      // try{Thread.sleep(1000);}catch(InterruptedException e){}
    }
  }
  public static void main(String arg[]){
    MultiThread th0 = new MultiThread();
    MultiThread th1 = new MultiThread();
    MultiThread th2 = new MultiThread();
    th0.start();
    th1.start();
    th2.start();
  }
}
