public class something{

  public static int getUmbrellas(int requirement, List<Integer> sizes) {
          if(sizes==null || sizes.isEmpty() || requirement<0) return -1;
          Collections.sort(sizes);
          int end = sizes.size() -1;
          int minUmbrellas=Integer.MAX_VALUE;
          while(end>=0){
              int noUmbrellas =0;
              int j = end--;
              int req = requirement;
              while(req>0 && j >=0){
                  noUmbrellas += req/ sizes.get(j);
                  req = requirement % sizes.get(j);
                  j--;
              }

              if(req==0) minUmbrellas = Math.min(noUmbrellas, minUmbrellas);
          }

          return minUmbrellas==Integer.MAX_VALUE ? -1 : minUmbrellas;

      // Write your code here

      }

      public static void main(String[] args) {
          System.out.println("ds");
      }

}
