//
//  TechCompaniesListViewController.swift
//  TechCompanies
//
//  Created by Electra Chong on 5/27/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class TechCompaniesListViewController: UITableViewController {
    
    var schoolList: [Entity]! = EntityHelper.getSchools()
    var techCompanyList: [Entity]! = EntityHelper.getTechCompanies()

    override func viewDidLoad() {
        super.viewDidLoad()
        self.title = "Entity list"

        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    /* Specify the number of sections to create */
    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return 2
    }
    
    /* Specify the number of rows in each section */
    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        let sections = section == 0 ? techCompanyList.count : schoolList.count
        return sections
    }
   
    /* Create the section titles */
    override func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        let sectionTitle = section == 0 ? "Tech Companies" : "Schools"
        return sectionTitle
    }
    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("techCell", forIndexPath: indexPath)

        // Configure the cell...
        if indexPath.section == 0 {
            cell.textLabel?.text = techCompanyList[indexPath.row].name
            cell.detailTextLabel?.text = "I love working"
        }
        else {
            cell.textLabel?.text = schoolList[indexPath.row].name
            cell.detailTextLabel?.text = "I love studying"
        }
        
        return cell
    }

    /*
    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
        
        let techDetailSegue = "techDetailSegue"
        
        if segue.identifier == techDetailSegue {
            let segueController = segue.destinationViewController as! TechCompanyDetailViewController

            let retrieved_entity = retrieve_entity(sender)
            if retrieved_entity != nil {
                segueController.entity = retrieved_entity
            }
            else {
                print("name of sender cell did not match any entity name")
            }
            
            
        }
    }
    
    func retrieve_entity(sender: AnyObject?) -> Entity? {
        for item in techCompanyList
        {
            if sender!.textLabel!!.text == item.name {
                return item
            }
        }
        for item in schoolList
        {
            if sender!.textLabel!!.text == item.name {
                return item
            }
            
        }
        return nil
    }

}
