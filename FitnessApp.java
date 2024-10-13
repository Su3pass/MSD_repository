package com.example;

import java.util.Scanner;

public class FitnessApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        TeachingService teachingService = new TeachingService();
        ShoppingService shoppingService = new ShoppingService();

        boolean running = true;
        while (running) {
            System.out.println("Welcome to the Fitness App!");
            System.out.println("1. View Fitness Teaching Videos");
            System.out.println("2. Purchase Fitness Products");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine();  // Consume newline

            switch (choice) {
                case 1:
                    teachingService.listVideos();
                    break;
                case 2:
                    shoppingService.listProducts();
                    shoppingService.purchaseProduct(scanner);
                    break;
                case 3:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }

        scanner.close();
    }
}