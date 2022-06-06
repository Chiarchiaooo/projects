package it.chiarchiaooo.McConsoleScanner;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

/**
 * @Author:Chiarchiaooo
 * @Description:Auto MC server log file scanner
 */


public class Main {

    int x = 0;
    Boolean dupe= false;
    final File dir = new File("output");



    public void read(String f) {
        try {
            Scanner s = new Scanner(new File(f));
            while (s.hasNext()) {
                System.out.println(s.nextLine());
            }
        } catch (FileNotFoundException e) {
            e.getStackTrace();
        }
    }

    public void check(String filename) {
        try {
            File outdir = new File(dir,filename);
            if (dir.exists()) {
                File subdir = new File(dir,filename + "-" + x);
                if (subdir.exists()) {
                    x++;
                    subdir.mkdir();
                    File fd = new File(subdir, filename);
                    fd.createNewFile();
                    check(filename);
                }else {
                    dupe = true;
                    subdir.mkdir();
                    read(filename);

                }
            }else {
                dir.mkdir();
                dupe = false;
                System.out.println("Setup completed");
                outdir.mkdir();
                File log = new File(outdir, filename);
                log.createNewFile();
            }
            
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    private void start() {
        File f = new File("");
        String filename = null;
        while (!f.exists()) {
            Scanner input = new Scanner(System.in);
            System.out.println("\nInsert file path");
            filename = input.nextLine();
            f = new File(filename);
        }
        check(filename);
    }





    public static void main(String[] args){
        //System.out.println("Welcome to MC console scanner, insert path to .log file");
            try {
                Main m = new Main();
                m.start();
            }catch (Exception e) {
                e.printStackTrace();
            }

        }
}


