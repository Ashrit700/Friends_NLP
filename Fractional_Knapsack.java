
import java.util.*;
public class ashrit {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        Double w=sc.nextDouble();
        Double[][] arr=new Double[n][2];
        for(int i=0;i<n;i++){
            arr[i][0]=sc.nextDouble();
            arr[i][1]=sc.nextDouble();
        }
        double[][]p=new double[n][2];
        for(int i=0;i<n;i++){
            p[i][0]=arr[i][0]/arr[i][1];
            p[i][1]=i;

        }
        Arrays.sort(p,(a,b)-> Double.compare(b[0],a[0]));
        double wieght=0;
        double ans=0;
        for(int i=0;i<n;i++){
            if(arr[(int)p[i][1]][1]+wieght<=w){
                ans=arr[(int)p[i][1]][0]+ans;
                wieght=wieght+arr[(int)p[i][1]][1];
            }
            else{
                double g=(w-wieght)/arr[i][1];
                ans=arr[(int)p[i][1]][0]*g+ans;
                System.out.println(g);
            }
        }

        System.out.println(ans+" ");

    }
}
