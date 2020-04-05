import java.io.File;
import java.io.FileOutputStream;

import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class WriteToExcel {
   public static void main(String[] args) throws Exception {

     BufferedReader br = null;
     //Create blank workbook
     XSSFWorkbook workbook = new XSSFWorkbook();

     //Create a blank sheet
     XSSFSheet spreadsheet = workbook.createSheet( " plots ");

     try {
 			String actionString;
 			br = new BufferedReader(new FileReader("forwardPlots.txt"));

      int i = 1;

 			while ((actionString = br.readLine()) != null) {

        //Create row object
        XSSFRow row;

        String[] arr = actionString.split();

        //This data needs to be written (Object[])
        Map < String, Object[] > empinfo = new TreeMap < String, Object[] >();
        empinfo.put( "i", new Object[] {
            arr[1], arr[0]});

        //Iterate over data and write to sheet
        Set < String > keyid = empinfo.keySet();
        int rowid = 0;

        for (String key : keyid) {
           row = spreadsheet.createRow(rowid++);
           Object [] objectArr = empinfo.get(key);
           int cellid = 0;

           for (Object obj : objectArr){
              Cell cell = row.createCell(cellid++);
              cell.setCellValue((String)obj);
           }
        }
        i++;
 			}
 		} catch (IOException e) {
 			e.printStackTrace();
 		} finally {
 			try {
 				if (br != null)br.close();
 			} catch (IOException ex) {
 				ex.printStackTrace();
 			}
 		}

    //Write the workbook in file system
    FileOutputStream out = new FileOutputStream(
       new File("./Writesheet.xlsx"));

    workbook.write(out);
    out.close();
    System.out.println("Writesheet.xlsx written successfully");
   }

}
