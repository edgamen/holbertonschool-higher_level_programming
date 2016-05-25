//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    var taps_done = 0
    var taps_requested = 0
    @IBOutlet weak var tapper: UIImageView!
    @IBOutlet weak var play_button: UIButton!
    @IBOutlet weak var coin: UIButton!
    @IBOutlet weak var taps_label: UILabel!
    @IBOutlet weak var request_field: UITextField!
    
    @IBAction func tapCoin(sender: AnyObject) {
    
        taps_done += 1
        updateTapsLabel()
        
        if taps_done > taps_requested {
            self.resetGame()
        }
    
    }
    
    @IBAction func tapPlay(sender: AnyObject) {
    
        if self.request_field != nil && self.request_field.text != "" {
            
            if Int(self.request_field.text!) != nil {
                taps_requested = Int(self.request_field.text!)!
                
                self.tapper.hidden = true
                self.play_button.hidden = true
                self.request_field.hidden = true
                
                self.taps_label.hidden = false
                self.coin.hidden = false
            }
            
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        self.resetGame()
    }
    
    func updateTapsLabel() {
        taps_label.text = String(taps_done) + " taps!"
    }
    
    func resetGame() {
        self.taps_done = 0
        self.taps_requested = 0
        self.request_field.text = ""
        
        updateTapsLabel()
        self.tapper.hidden = false
        self.play_button.hidden = false
        self.request_field.hidden = false
        
        self.taps_label.hidden = true
        self.coin.hidden = true
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

