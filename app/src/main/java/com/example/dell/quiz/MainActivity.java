package com.example.dell.quiz;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;
public class MainActivity extends AppCompatActivity {
    int count;
    public String correctAnswer = "21";
    public EditText edit_Text;
    public CheckBox checkb1;
    public CheckBox checkb2;
    public CheckBox checkb3;
    public RadioButton radioQ3;
    public RadioButton radioQ4;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    //cheeck Q1, the answer is 6,4 and should click both 6,2 without 3 to get +1
    public int onCheckboxClicked() {
        checkb1 = findViewById(R.id.chb1);
        checkb2 = findViewById(R.id.chb2);
        checkb3 = findViewById(R.id.chb3);
        if (checkb1.isChecked() && checkb2.isChecked() && !checkb3.isChecked()) {
            count++;
        }
        return count;
    }
    //check for Q2 if edit_text = correctAnswer will take +1
    public int onWriteText() {
        edit_Text = findViewById(R.id.editText);
        String Answer = edit_Text.getText().toString();
        if (Answer.contentEquals(correctAnswer)) {
            count++;
        }
        return count;
    }
    //check for Q3,Q4 if answer No +1 for each question
    public int onRadioButtonClicked() {
        radioQ3 = findViewById(R.id.radioaQ3);
        radioQ4 = findViewById(R.id.radioaQ4);
        if (radioQ3.isChecked()) {
            count++;
        }
        if (radioQ4.isChecked()) {
            count++;
        }
        return count;
    }
    //reset all answers and score
    public void resetScore() {
        checkb1.setChecked(false);
        checkb2.setChecked(false);
        checkb3.setChecked(false);
        RadioGroup radiob1 = findViewById(R.id.Group1);
        radiob1.clearCheck();
        RadioGroup radiob3 = findViewById(R.id.Group2);
        radiob3.clearCheck();
        edit_Text.setText(null);
        count = 0;
    }
    //when click on sumbit it to will ckeck the answer then print score then rest answer to repeat the quiz
    public void SumbitQuiz(View view) {
        onCheckboxClicked();
        onWriteText();
        onRadioButtonClicked();
        Toast.makeText(this, "Score:" + count + "/ 4", Toast.LENGTH_SHORT).show();
        resetScore();
    }
}