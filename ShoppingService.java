package com.example;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class ShoppingService {
    private List<Product> products;

    public ShoppingService() {
        // 初始化一些商品（在实际应用中，这些可能来自数据库）
        products = Arrays.asList(
                new Product("Resistance Bands", 19.99),
                new Product("Yoga Mat", 29.99),
                new Product("Dumbbells", 49.99)
        );
    }

    public void listProducts() {
        System.out.println("Available Fitness Products:");
        for (int i = 0; i < products.size(); i++) {
            Product product = products.get(i);
            System.out.println((i + 1) + ". " + product.getName() + " - $" + product.getPrice());
        }
    }

    public void purchaseProduct(Scanner scanner) {
        System.out.print("Enter the product number to purchase: ");
        int choice = scanner.nextInt();
        scanner.nextLine();  // Consume newline

        if (choice > 0 && choice <= products.size()) {
            Product product = products.get(choice - 1);
            System.out.println("You have chosen to purchase: " + product.getName());
            // 在实际应用中，这里会添加购买逻辑，如更新库存、处理支付等
            System.out.println("Purchase successful! Thank you for shopping with us.");
        } else {
            System.out.println("Invalid product number. Please try again.");
        }
    }

    // Product类定义
    private static class Product {
        private String name;
        private double price;

        public Product(String name, double price) {
            this.name = name;
            this.price = price;
        }

        public String getName() {
            return name;
        }

        public double getPrice() {
            return price;
        }
    }
}