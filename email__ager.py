#!/usr/bin/env python3
"""
The Magnificent Email Ager - A Completely Useless Machine
=========================================================

Takes your precious emails, sends them on a pointless journey through 
time and space (well, mostly time), then delivers them slightly worse
for wear. Like a fine wine, but backwards.

Features:
- Unnecessary complexity ✓
- Performative delays ✓  
- Over-engineered logging ✓
- Configurable pointlessness ✓
- ASCII art because why not ✓
"""

import smtplib
import imaplib
import email
import time
import random
import threading
import json
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dataclasses import dataclass
from typing import List, Optional
import logging

# Configure unnecessarily verbose logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('EmailAger')

@dataclass
class AgingEmail:
    """An email in the process of becoming magnificently aged"""
    id: str
    sender: str
    recipient: str
    subject: str
    body: str
    original_timestamp: datetime
    aging_duration: int  # minutes
    loop_count: int = 0
    flavor_notes: List[str] = None
    
    def __post_init__(self):
        if self.flavor_notes is None:
            # Generate pretentious aging descriptors
            flavors = [
                "hints of procrastination", "notes of digital decay", 
                "undertones of temporal displacement", "a bouquet of delayed gratification",
                "whispers of electronic entropy", "traces of bandwidth anxiety",
                "essence of server lag", "subtle oxidation of urgency"
            ]
            self.flavor_notes = random.sample(flavors, random.randint(2, 4))

class EmailAger:
    """The most unnecessary email processing system ever conceived"""
    
    def __init__(self, config_file: str = "ager_config.json"):
        self.config = self._load_config(config_file)
        self.aging_chamber = []  # Our precious aging emails
        self.is_aging = False
        self.ascii_art()
        
    def ascii_art(self):
        """Because every useless machine needs ASCII art"""
        art = """
╔══════════════════════════════════════════════════════════╗
║                    EMAIL AGER 3000™                     ║
║            "Making Email Worse Since Today"             ║
║                                                          ║
║    📧 ──→ [AGING CHAMBER] ──→ ⏰ ──→ 📧 (but older)    ║
║                                                          ║
║              ⚡ MAXIMUM INEFFICIENCY ⚡                  ║
╚══════════════════════════════════════════════════════════╝
        """
        print(art)
        
    def _load_config(self, config_file: str) -> dict:
        """Load configuration or create a delightfully useless default"""
        default_config = {
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587,
            "imap_server": "imap.gmail.com", 
            "imap_port": 993,
            "username": "your_email@gmail.com",
            "password": "your_app_password",
            "aging_folder": "INBOX/EmailAger",
            "min_aging_time": 30,  # minutes
            "max_aging_time": 1440,  # 24 hours
            "pointless_loops": True,
            "verbose_aging": True,
            "pretentious_mode": True
        }
        
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                # Merge with defaults
                for key, value in default_config.items():
                    config.setdefault(key, value)
                return config
        except FileNotFoundError:
            logger.info(f"Config file not found, creating default: {config_file}")
            with open(config_file, 'w') as f:
                json.dump(default_config, f, indent=2)
            return default_config
    
    def pointless_loop_delay(self, duration_minutes: int):
        """Perform completely unnecessary work while aging email"""
        logger.info(f"🔄 Beginning pointless aging loops for {duration_minutes} minutes...")
        
        end_time = datetime.now() + timedelta(minutes=duration_minutes)
        loop_counter = 0
        
        while datetime.now() < end_time:
            loop_counter += 1
            
            # Perform magnificently useless calculations
            useless_work = sum(i ** 2 for i in range(1000)) % 42
            
            # Generate aging status updates
            remaining = int((end_time - datetime.now()).total_seconds() / 60)
            
            if self.config["verbose_aging"]:
                status_updates = [
                    f"Loop {loop_counter}: Aging in progress... {remaining}m remaining",
                    f"Loop {loop_counter}: Email developing character... {remaining}m left",
                    f"Loop {loop_counter}: Temporal seasoning applied... {remaining}m to go",
                    f"Loop {loop_counter}: Digital patina forming... {remaining}m remaining"
                ]
                logger.info(random.choice(status_updates))
            
            # Sleep for a random interval to add chaos
            time.sleep(random.uniform(10, 30))
            
        logger.info(f"✨ Aging complete after {loop_counter} magnificently pointless loops!")
        return loop_counter
    
    def age_email_content(self, email_obj: AgingEmail) -> str:
        """Add 'aging' artifacts to email content"""
        aged_body = email_obj.body
        
        if self.config["pretentious_mode"]:
            # Add aging certificate
            aging_cert = f"""
            
╔════════════════════════════════════════════════════════════════╗
║                    AGING CERTIFICATE                           ║
║                                                                ║
║ This email has been aged for {email_obj.aging_duration} minutes in our      ║
║ premium digital aging chambers.                                ║
║                                                                ║
║ Flavor Profile: {', '.join(email_obj.flavor_notes[:2])}        ║
║ Loop Count: {email_obj.loop_count} unnecessary iterations                  ║
║ Aged: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                       ║
║                                                                ║
║        🍷 "Like fine wine, but for electrons" 🍷               ║
╚════════════════════════════════════════════════════════════════╝
            """
            aged_body += aging_cert
            
        # Add subtle "aging" effects
        if random.random() < 0.3:  # 30% chance
            aged_body += "\n\n[This email may have developed slight digital oxidation during aging]"
            
        return aged_body
    
    def send_aged_email(self, email_obj: AgingEmail):
        """Finally send the magnificently aged email"""
        try:
            # Create the aged email
            msg = MIMEMultipart()
            msg['From'] = email_obj.sender
            msg['To'] = email_obj.recipient
            msg['Subject'] = f"[AGED {email_obj.aging_duration}m] {email_obj.subject}"
            
            aged_body = self.age_email_content(email_obj)
            msg.attach(MIMEText(aged_body, 'plain'))
            
            # Send via SMTP
            with smtplib.SMTP(self.config['smtp_server'], self.config['smtp_port']) as server:
                server.starttls()
                server.login(self.config['username'], self.config['password'])
                server.send_message(msg)
                
            logger.info(f"📬 Successfully delivered aged email: '{email_obj.subject}'")
            logger.info(f"   Flavor notes: {', '.join(email_obj.flavor_notes)}")
            
        except Exception as e:
            logger.error(f"Failed to deliver aged email: {e}")
    
    def age_email(self, sender: str, recipient: str, subject: str, body: str, 
                  aging_minutes: Optional[int] = None):
        """Begin the magnificent aging process"""
        
        if aging_minutes is None:
            aging_minutes = random.randint(
                self.config['min_aging_time'], 
                self.config['max_aging_time']
            )
        
        email_obj = AgingEmail(
            id=f"aged_{int(time.time())}_{random.randint(1000, 9999)}",
            sender=sender,
            recipient=recipient,
            subject=subject,
            body=body,
            original_timestamp=datetime.now(),
            aging_duration=aging_minutes
        )
        
        logger.info(f"🍷 Beginning aging process for email: '{subject}'")
        logger.info(f"   Aging duration: {aging_minutes} minutes")
        logger.info(f"   Expected flavor profile: {', '.join(email_obj.flavor_notes)}")
        
        # Start aging in a separate thread so we can age multiple emails
        aging_thread = threading.Thread(
            target=self._aging_worker, 
            args=(email_obj,),
            daemon=True
        )
        aging_thread.start()
        
        return email_obj.id
    
    def _aging_worker(self, email_obj: AgingEmail):
        """The worker that performs the actual aging"""
        # Perform pointless loops
        if self.config["pointless_loops"]:
            email_obj.loop_count = self.pointless_loop_delay(email_obj.aging_duration)
        else:
            # Even if pointless loops are disabled, we still wait
            logger.info(f"⏰ Aging email '{email_obj.subject}' for {email_obj.aging_duration} minutes...")
            time.sleep(email_obj.aging_duration * 60)
        
        # Send the aged email
        self.send_aged_email(email_obj)
    
    def batch_age_emails(self, emails: List[dict]):
        """Age multiple emails simultaneously"""
        logger.info(f"🏭 Starting batch aging of {len(emails)} emails...")
        
        for email_data in emails:
            self.age_email(**email_data)
    
    def get_aging_status(self):
        """Get status of all aging emails (if we were tracking them)"""
        return {
            "active_aging_processes": threading.active_count() - 1,
            "total_aged_today": "¯\\_(ツ)_/¯",  # We're too useless to track this
            "pointlessness_level": "MAXIMUM"
        }

# Example usage and testing
if __name__ == "__main__":
    ager = EmailAger()
    
    # Example: Age a single email
    email_id = ager.age_email(
        sender="test@example.com",
        recipient="friend@example.com", 
        subject="Important Business Proposal",
        body="Dear Friend,\n\nThis email will be much better after aging.\n\nBest regards,\nThe Sender",
        aging_minutes=2  # 2 minutes for testing
    )
    
    print(f"\n🎉 Email queued for aging with ID: {email_id}")
    print("📊 Current status:", ager.get_aging_status())
    
    # Example: Batch aging
    batch_emails = [
        {
            "sender": "boss@company.com",
            "recipient": "employee@company.com",
            "subject": "Urgent Meeting Request", 
            "body": "We need to meet urgently about the thing.",
            "aging_minutes": 1
        },
        {
            "sender": "spam@nowhere.com",
            "recipient": "victim@example.com",
            "subject": "You've Won a Million Dollars!",
            "body": "Congratulations! You've won! Send us your bank details!",
            "aging_minutes": 3  # Spam deserves extra aging
        }
    ]
    
    ager.batch_age_emails(batch_emails)
    
    print("\n🚀 All emails are now aging magnificently!")
    print("💡 Pro tip: The longer they age, the more sophisticated they become!")
    print("🎭 Watch the logs for delightfully unnecessary status updates!")
    
    # Keep the main thread alive to see aging in action
    try:
        while threading.active_count() > 1:
            time.sleep(10)
            print(f"⏳ Still aging... ({threading.active_count() - 1} active processes)")
    except KeyboardInterrupt:
        print("\n🛑 Aging interrupted! Some emails may be under-aged!")