package com.example;

import java.util.Arrays;
import java.util.List;

public class TeachingService {
    private List<String> videoTitles;

    public TeachingService() {
        // 初始化一些健身教学视频标题（在实际应用中，这些可能来自数据库）
        videoTitles = Arrays.asList("Yoga for Beginners", "Strength Training 101", "Cardio Workouts");
    }

    public void listVideos() {
        System.out.println("Available Fitness Teaching Videos:");
        for (int i = 0; i < videoTitles.size(); i++) {
            System.out.println((i + 1) + ". " + videoTitles.get(i));
        }
    }

    // 这里可以添加更多方法来处理视频观看、下载等
}